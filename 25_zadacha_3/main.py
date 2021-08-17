from dict import MyDict

classic_dict = {
    'name': 12,
    'valera': 13,
    'petro': 20
}

new_dict = MyDict({'name': 12,
                   'valera': 13,
                   'petro': 20
                   })


print(classic_dict)
print(new_dict)

print(classic_dict.get('name'))
print(new_dict.get('name'))

print(classic_dict.get('namse'))
print(new_dict.get('namse'))