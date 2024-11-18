import pytest


# Este hook agrega una columna con el ID personalizado a la tabla de resultados
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, 'Test ID')  # Agrega una nueva columna "Test ID" en el encabezado


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report, cells):
    # Accedemos al item, que es donde están los marcadores
    item = report.nodeid

    # Ensure 'item' is a function or method before calling 'get_closest_marker'
    if hasattr(item, 'get_closest_marker'):
        marker = item.get_closest_marker("test_id")

        # Si encontramos un marcador 'test_id', extraemos su valor
        if marker:
            test_id = marker.args[0]  # El primer argumento del marcador 'test_id'
        else:
            test_id = "No ID"  # Si no hay marcador, asignamos un valor por defecto

        # Insertamos el ID en la celda correspondiente de la fila
        cells.insert(2, test_id)
    else:
        # Handle cases where 'item' is not a test function/method
        test_id = "N/A"  # Or any other suitable value
        cells.insert(2, test_id)