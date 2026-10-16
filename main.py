
import glfw
from OpenGL.GL import *


def desenhar_cubo():
    # Cada face do cubo possui uma cor diferente
    faces = [
        ((1, 0, 0), [(-1,-1, 1), (1,-1, 1), (1, 1, 1), (-1, 1, 1)]),
        ((0, 1, 0), [(-1,-1,-1), (-1, 1,-1), (1, 1,-1), (1,-1,-1)]),
        ((0, 0, 1), [(-1,-1,-1), (-1,-1, 1), (-1, 1, 1), (-1, 1,-1)]),
        ((1, 1, 0), [(1,-1,-1), (1, 1,-1), (1, 1, 1), (1,-1, 1)]),
        ((1, 0, 1), [(-1, 1,-1), (-1, 1, 1), (1, 1, 1), (1, 1,-1)]),
        ((0, 1, 1), [(-1,-1,-1), (1,-1,-1), (1,-1, 1), (-1,-1, 1)])
    ]

    glBegin(GL_QUADS)

    for cor, vertices in faces:
        glColor3f(*cor)

        for vertice in vertices:
            glVertex3f(*vertice)

    glEnd()


def main():
    if not glfw.init():
        raise RuntimeError("Falha ao inicializar GLFW")

    # Solicita um contexto OpenGL compatível com desenho imediato
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)

    window = glfw.create_window(
        800, 600,
        "Meu primeiro objeto 3D",
        None, None
    )

    if not window:
        glfw.terminate()
        raise RuntimeError("Falha ao criar janela")

    glfw.make_context_current(window)

    # Habilita o teste de profundidade para objetos 3D
    glEnable(GL_DEPTH_TEST)

    # Define a projeção e o enquadramento da cena
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.5, 1.5, -1.125, 1.125, 2, 20)

    glMatrixMode(GL_MODELVIEW)

    while not glfw.window_should_close(window):
        glClearColor(0.12, 0.16, 0.22, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        # Afasta o cubo da câmera para que fique visível
        glTranslatef(0.0, 0.0, -6.0)

        # Inclina o cubo para revelar várias faces
        glRotatef(25, 1, 0, 0)
        glRotatef(35, 0, 1, 0)

        desenhar_cubo()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
