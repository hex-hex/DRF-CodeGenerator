import itertools
import jinja2
from enum import Enum
from operator import itemgetter
import re


class VarType(Enum):
    Unknown = 0
    StringField = 1
    NumberField = 2
    ForeignKey = 3
    ManyToManyKey = 4


class CodeType(Enum):
    DEFINE_CLASS = 1
    DEFINE_FUNC = 2
    DEFINE_VAR = 3
    DEFINE_FLOW = 4


KEY_MAP = {
    'models.FileField': VarType.StringField,
    'models.CharField': VarType.StringField,
    'models.DateField': VarType.StringField,
    'models.BooleanField': VarType.StringField,
    'models.EmailField': VarType.StringField,
    'models.IntegerField': VarType.NumberField,
    'models.FloatField': VarType.NumberField,
    'models.PositiveIntegerField': VarType.NumberField,
    'models.ForeignKey': VarType.ForeignKey,
    'models.ManyToManyField': VarType.ManyToManyKey,
}

DEFINE_MAP = {
    'def': CodeType.DEFINE_FUNC,
    'class': CodeType.DEFINE_CLASS,
    'if': CodeType.DEFINE_FLOW,
    'while': CodeType.DEFINE_FLOW,
    'for': CodeType.DEFINE_FLOW,
}


class IndentCode:
    def __init__(self, code_line):
        self.code = code_line.rstrip()
        self.indent = sum(1 for _ in itertools.takewhile(str.isspace, self.code))
        self.code = self.code.strip()
        self.words = list(filter(lambda x: len(x) > 0, self.code.split(' ')))
        # self.var_names = []
        self.type = None
        try:
            self.type = DEFINE_MAP[self.words[0]]
        except KeyError:
            self.type = CodeType.DEFINE_VAR
        except Exception as ex:
            pass

    def parse_class(self):
        try:
            assert self.type == CodeType.DEFINE_CLASS
            class_name = list(itertools.takewhile(lambda x: '(' != x, self.words[1]))
            class_name = ''.join(class_name)
            class_parents = self.words[1].strip(class_name).strip(':').strip('(').strip(')').split(',')
            return class_name, class_parents
        except Exception:
            return '', ''

    def parse_var(self):
        try:
            assert self.type == CodeType.DEFINE_VAR
            var_names = list(itertools.takewhile(lambda x: '=' not in x, self.words))
            var_names = '' if '' in var_names else var_names
            type_def = list(itertools.dropwhile(lambda x: '=' not in x, self.words))[1]
            type_def = list(itertools.takewhile(lambda x: '(' != x, type_def))
            type_def = ''.join(type_def)
            type_def = KEY_MAP[type_def]
            reg_param = re.compile('\'[A-Z][a-z]+\'')
            var_params = list(map(lambda x: reg_param.search(x).group(0).strip('\'') if reg_param.search(x) else '', self.words))
            var_params = list(filter(lambda x: len(x) > 0, var_params))
            return var_names, type_def, var_params
        except Exception as ex:
            return '', VarType.Unknown, []

    def if_empty(self):
        return len(self.code) == 0


class EntityCode:
    CONTINUE_END = ('\\', ',', '(', '{', '[', '.', '+')
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/'))

    def has_base(self):
        'EntityBase' in self.entity_base

    def toCamel(self, snake_name):
        return ''.join([word.capitalize() for word in snake_name.split('_')])

    def toLowerCamel(self, snake_name):
        snake_name = self.toCamel(snake_name)
        return snake_name[0].lower() + snake_name[1:]

    def __init__(self, _code):
        self.codes = _code.split('\n')
        self.codes = list(filter(lambda x: len(x) != 0 and not x.isspace(), self.codes))

        for idx in range(len(self.codes) - 1):
            if self.codes[idx][-1] in self.CONTINUE_END:
                self.codes[idx + 1] = self.codes[idx] + self.codes[idx + 1].strip()
                self.codes[idx] = ''

        self.codes = list(filter(lambda x: len(x) != 0 and not x.isspace(), self.codes))
        self.codes = [IndentCode(x) for x in self.codes]
        self.code_tree = itertools.groupby(self.codes, key=lambda x: x.indent)
        self.code_tree = [(indent, list(body)) for indent, body in self.code_tree]
        self.code_tree = sorted(self.code_tree, key=itemgetter(0))

        def_line = self.code_tree[0][1][0]
        self.entity_name, self.entity_base = def_line.parse_class()
        self.var_lines = self.code_tree[1][1]

        self.child_vars = [x.parse_var() for x in self.var_lines]
        self.child_vars = list(filter(lambda x: x[1] != VarType.Unknown, self.child_vars))
        self.child_vars = sorted(self.child_vars, key=lambda x: x[1].value)
        self.child_vars = itertools.groupby(self.child_vars, key=itemgetter(1))
        self.child_vars = [(var_type.value, [(var_body[0][0], var_body[2]) for var_body in list(var_declare)]) for
                           var_type, var_declare in self.child_vars]
        self.child_vars = dict(self.child_vars)

        service_output = self.jinja_env.get_template('all.py').render({'modelFields': self})
        print(service_output)

        with open('./kotlin_model/{}.kt'.format(self.toCamel(self.entity_name)), 'w+') as file:
            model_output = self.jinja_env.get_template('model.kt') .render({'modelFields': self})
            file.write(model_output)


