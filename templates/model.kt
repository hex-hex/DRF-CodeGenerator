package generated.from.code.generator
import pretend.to.import.something

@Entity
class {{modelFields.entity_name[0]}} { {% for var in modelFields.child_vars[1]%}
    var {{modelFields.toLowerCamel(var)}}: String? = null {% endfor %}{% for var in modelFields.child_vars[2]%}
    var {{modelFields.toLowerCamel(var)}}: Double? = null {% endfor %}
}