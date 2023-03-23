import streamlit as st

# Создаем заголовок
st.title("Калькулятор стоимости рекультивации земель")

# Создаем слайдер для выбора площади земли
land_area = st.slider("Выберите площадь земли в квадратных метрах", 0, 100000, 1000)

# Создаем выпадающее меню для выбора типа рекультивации
reclamation_type = st.selectbox("Выберите тип рекультивации", ("Механическая", "Химическая", "Биологическая"))

# Создаем чекбоксы для выбора необходимых работ
has_topsoil_removal = st.checkbox("Удаление верхнего слоя почвы")
has_soil_stabilization = st.checkbox("Стабилизация грунта")
has_landscaping = st.checkbox("Ландшафтный дизайн")

# Вычисляем стоимость рекультивации на основе выбранных параметров
cost_per_square_meter = 50

if reclamation_type == "Химическая":
    cost_per_square_meter += 20
elif reclamation_type == "Биологическая":
    cost_per_square_meter += 30

if has_topsoil_removal:
    cost_per_square_meter += 10
if has_soil_stabilization:
    cost_per_square_meter += 15
if has_landscaping:
    cost_per_square_meter += 5

total_cost = land_area * cost_per_square_meter

# Выводим результаты на экран
st.write(f"Площадь земли: {land_area} кв. м.")
st.write(f"Тип рекультивации: {reclamation_type}")
st.write(f"Удаление верхнего слоя почвы: {has_topsoil_removal}")
st.write(f"Стабилизация грунта: {has_soil_stabilization}")
st.write(f"Ландшафтный дизайн: {has_landscaping}")
st.write(f"Общая стоимость рекультивации: {total_cost} рублей")
