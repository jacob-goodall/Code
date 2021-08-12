example=['130','90','150','123','133','120','160','45','67','55','34']
sub_lists=[['130','90','150'],['90','150'],['120','160','45','67']]
result = []
for sub in sub_lists:
    result.append([example.index(sub[0]),example.index(sub[-1])])
print(result)