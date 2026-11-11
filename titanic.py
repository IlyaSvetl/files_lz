import pandas as ps
import matplotlib.pyplot as plt
df = ps.read_parquet("titanic.parquet") #  Чтение parquet
df.to_csv("titanic.csv", index=False)#  Сохранение в CSV в папку
print("Файл titanic.csv сохранён")
titanic = ps.read_csv("titanic.csv")#  чтение CSV и построение гистограммы выживаемости

# Определяем названия колонок (Pclass, Survived)
# Если названия отличаются — при необходимости замените.
pclass_col = "Pclass" if "Pclass" in titanic.columns else "pclass"
survived_col = "Survived" if "Survived" in titanic.columns else "survived"
survival_by_class = titanic.groupby([pclass_col, survived_col]).size().unstack(fill_value=0) # Группировка: количество выживших и невыживших по классам
survival_by_class.columns = ["Не выжил", "Выжил"][: len(survival_by_class.columns)] # Переименуем для наглядности
if list(survival_by_class.columns) == [0, 1]:
    survival_by_class.columns = ["Не выжил", "Выжил"]

# Построение гистограммы
b = survival_by_class.plot( kind="bar", figsize=(7, 4), color=["#d62728", "#2ca02c"], edgecolor="black",)
b.set_title("Выживаемость пассажиров Титаника по классу билета")
b.set_xlabel("Класс билета")
b.set_ylabel("Количество пассажиров")
b.set_xticklabels([f"{int(x)} класс" for x in survival_by_class.index], rotation=0)
b.legend(title="Статус")
plt.tight_layout()
plt.savefig("survival_by_class.png", dpi=150)
plt.show()