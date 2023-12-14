## Вступ

Цей проект реалізує інтерполяційний поліном Ньютона для заданих точок. Застосовується алгоритм обчислення різниць та метод Ньютона для знаходження коефіцієнтів поліному.

## Вимоги

Для використання цього проекту потрібно мати встановлені наступні бібліотеки:

- NumPy
- Matplotlib
- Pandas

Їх можна встановити за допомогою команди:

bash
pip install numpy matplotlib

Використання:
Відкрийте файл tests\test_lagrange.py та змініть шлях в sys.path.append('G:\Ilya\interpolation_pkg') 
також у інших файлах

Вхідні дані Вхідні дані представлені у вигляді масивів x та y, які визначають координати точок.

x = np.array([0, 0.5, 1, 2, 3.5, 4, 5])
y = np.array([12.234, 9.239, 8.567, -1.098, 5.756, 7.345, 5.678])


Автор: [Процюк Юрій і Бичков Ілля]
