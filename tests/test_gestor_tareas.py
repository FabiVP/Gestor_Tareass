import unittest
from src.logica.Gestor_Tareass import GestorTareas
class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].titulo, "Tarea 1")
        self.assertEqual(self.gestor.tareas[0].descripcion, "Descripción de la tarea 1")

    def test_agregar_tarea_sin_titulo(self):
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea("", "Descripción")

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.marcar_completada(0)
        self.assertTrue(self.gestor.tareas[0].completada)

    def test_marcar_completada_indice_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.gestor.marcar_completada(0)  # No hay tareas para marcar

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1", "Descripción de la tarea 1")
        self.gestor.eliminar_tarea(0)
        self.assertEqual(len(self.gestor.tareas), 0)

    def test_eliminar_tarea_indice_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.gestor.eliminar_tarea(0)  # No hay tareas para eliminar

if __name__ == "__main__":
    unittest.main()