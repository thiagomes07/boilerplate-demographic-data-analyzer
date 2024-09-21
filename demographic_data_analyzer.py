import pandas as pd

def calculate_demographic_data(print_data=True):
    # Lê os dados do arquivo CSV
    df = pd.read_csv("adult.data.csv")

    # 1. Quantidade de pessoas de cada raça representadas no dataset
    race_count = df['race'].value_counts()

    # 2. Qual é a idade média dos homens?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. Qual é a porcentagem de pessoas que têm um diploma de Bacharel?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # 4. Porcentagem de pessoas com educação avançada que ganham mais de 50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[higher_education]['salary'] == '>50K').mean() * 100

    # 5. Porcentagem de pessoas sem educação avançada que ganham mais de 50K
    lower_education = ~higher_education
    lower_education_rich = (df[lower_education]['salary'] == '>50K').mean() * 100

    # 6. Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentagem de pessoas que trabalham o mínimo de horas por semana e ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

    # 8. Qual país tem a maior porcentagem de pessoas que ganham >50K?
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack(fill_value=0)
    
    # Calcular a porcentagem de pessoas que ganham >50K por país
    country_salary_percentage = (country_salary['>50K'] / country_salary.sum(axis=1)) * 100
    
    # Encontrar o país com a maior porcentagem
    highest_earning_country_percentage = country_salary_percentage.max()
    highest_earning_country = country_salary_percentage.idxmax()

    # 9. Identificar a ocupação mais popular para aqueles que ganham >50K na Índia.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Impressão dos resultado
    if print_data:
        print("Número de cada raça:\n", race_count)
        print("Idade média dos homens:", round(average_age_men, 1))
        print(f"Porcentagem com diplomas de Bacharel: {round(percentage_bachelors, 1)}%")
        print(f"Porcentagem com educação superior que ganham >50K: {round(higher_education_rich, 1)}%")
        print(f"Porcentagem sem educação superior que ganham >50K: {round(lower_education_rich, 1)}%")
        print(f"Número mínimo de horas trabalhadas: {min_work_hours} horas/semana")
        print(f"Porcentagem rica entre aqueles que trabalham poucas horas: {round(rich_percentage, 1)}%")
        print("País com a maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos no país: {round(highest_earning_country_percentage, 1)}%")
        print("Ocupações mais populares na Índia:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }