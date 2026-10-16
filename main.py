import glfw
from OpenGL.GL import glClearColor, glClear, GL_COLOR_BUFFER_BIT

def main():
    # inicializa o GLFW
    if not glfw.init():
        raise RuntimeError("Não foi possível inicializar o GLFW")

    # cria a janela
    window = glfw.create_window(800,600,"Meu primeiro projeto OpenGL", None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("Não foi possível criar a janela")

    # ativa o contexto OpenGL da janela
    glfw.make_context_current(window)

    # define a cor de fundo: vermelho. verde, azul e opacidade
    glClearColor(0.12,0.16,0.22,1.0)

    # loop principal da aplicação
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    # encerra o GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()