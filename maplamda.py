
fields = []
fields.append('age')
fields.append('name')
fields.append('createTime')
escaped_fields = list(map(lambda f:'`%s`' % f, fields))

print(escaped_fields)

select = 'select `%s`, %s from `%s`' % ('id', ', '.join(escaped_fields), 'user')

print(select)
