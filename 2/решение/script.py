# функция для создания пар
def make_pairs(boys, girls):
    # сортируем списки
        boys_sorted = sorted(boys)
            girls_sorted = sorted(girls)
                
                    # проверка на равенство длин списков
                        if len(boys) != len(girls):
                                return "Внимание, кто-то может остаться без пары."
                                    
                                        # создание пар
                                            pairs = list(zip(boys_sorted, girls_sorted))
                                                
                                                    # формирование результата
                                                        result = "Идеальные пары:\n"
                                                            for pair in pairs:
                                                                    result += f"{pair[0]} и {pair[1]}\n"
                                                                        
                                                                            return result

                                                                            # примеры использования
                                                                            boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
                                                                            girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

                                                                            print(make_pairs(boys1, girls1))

                                                                            boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
                                                                            girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

                                                                            print(make_pairs(boys2, girls2))
                                                                            