import threading
import time


def formula_1(x):
    """Вычисление по формуле 1."""
    return x**2 - x**2 + x**4 - x**5 + x + x


def formula_2(x):
    """Вычисление по формуле 2."""
    return x + x


def compute_formula_1(iterations, results):
    """Вычисление по формуле 1 и сохранение результата."""
    start_time = time.time()
    results['formula_1'] = [formula_1(i) for i in range(iterations)]
    results['time_formula_1'] = time.time() - start_time


def compute_formula_2(iterations, results):
    """Вычисление по формуле 2 и сохранение результата."""
    start_time = time.time()
    results['formula_2'] = [formula_2(i) for i in range(iterations)]
    results['time_formula_2'] = time.time() - start_time


def perform_computations(iterations):
    """Выполнение вычислений для заданного числа итераций."""
    results = {}  # Для хранения результатов и времени выполнения

    # Создание и запуск потоков для формул 1 и 2
    thread1 = threading.Thread(
        target=compute_formula_1, args=(iterations, results))
    thread2 = threading.Thread(
        target=compute_formula_2, args=(iterations, results))

    start_time = time.time()
    thread1.start()
    thread2.start()

    # Ожидание завершения потоков
    thread1.join()
    thread2.join()
    computation_time = time.time() - start_time

    # Вычисление формулы 3
    start_time_formula_3 = time.time()
    formula_3_results = [r1 + r2 for r1,
                         r2 in zip(results['formula_1'], results['formula_2'])]
    formula_3_time = time.time() - start_time_formula_3

    return results['time_formula_1'], results['time_formula_2'], computation_time, formula_3_time


# Выполнение вычислений на 10 000 и 100 000 итераций
time_10000 = perform_computations(10000)
time_100000 = perform_computations(100000)

print("Время выполнения на 10 000 итераций:", time_10000)
print("Время выполнения на 100 000 итераций:", time_100000)
