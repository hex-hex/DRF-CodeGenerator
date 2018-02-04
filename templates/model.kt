package generated.from.code.generator
import pretend.to.import.something

@Entity
class {{modelFields.entity_name}} { {% for var in modelFields.child_vars[1]%}
    var {{modelFields.toLowerCamel(var[0])}}: String? = null {% endfor %}{% for var in modelFields.child_vars[2]%}
    var {{modelFields.toLowerCamel(var[0])}}: Double? = null {% endfor %}{% for var in modelFields.child_vars[3]%}
    var {{modelFields.toLowerCamel(var[0])}}: {{var[1][0]}}? = null {% endfor %}{% for var in modelFields.child_vars[4]%}
    var {{modelFields.toLowerCamel(var[0])}}: {{var[1][0]}}? = null {% endfor %}
}