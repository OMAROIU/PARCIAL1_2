# Proyecto Transporte Público - Programación Computacional III

## Integrantes
- OMAR SALVADOR GARCIA VASQUEZ
- FLOR MARINA TORES JANDRES

---

## Preguntas y Respuestas

### 1. ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?
Separar el código en módulos permite **organizar mejor el proyecto**, facilita el **mantenimiento** y la **reutilización** de las clases.  
Por ejemplo, si queremos mejorar la clase `Viaje`, lo hacemos en un solo archivo sin tocar `main.py`.

### 2. ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas.
Se crearon las siguientes clases:
- **Viaje** → representa un viaje con su ruta, costo, tiempo y día.  
- **Usuario** → representa una persona que puede registrar varios viajes.  
- **GestorUsuarios** → administra todos los usuarios y sus viajes.  

Esto aplica **encapsulamiento y abstracción**, representando el problema con objetos de la vida real.

### 3. ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto.
GitHub permitió que los integrantes trabajaran en paralelo.  
Por ejemplo, un miembro podía desarrollar la clase `Viaje` mientras el otro trabajaba en `Usuario`.  
Luego, con **git push y pull**, integraban cambios fácilmente, evitando sobreescribir el trabajo del compañero y manteniendo un historial de versiones.

---
