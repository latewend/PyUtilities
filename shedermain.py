from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram,compileShader
import numpy as np
from PIL import Image,ImageChops
import ctypes
import sdl2



WIDTH = 800
HIGHT = 800
Tloc = None
shaderProgram = None
TEXT = None
VAO = None
VBO = None
EBO = None
def init():
    global shaderProgram
    global VAO
    global VBO
    global EBO
    global Tloc 


    vertices = (
            0.5, -0.5,
            -0.5, -0.5,
            0.5,  0.5,
            -0.5,  0.5
        )
    randcolor = (
            0.5, 1,
            -0.5, -0.5,
            0.5,  0.5,
            -0.5,  0.5
        )
    vertices = np.array(vertices, dtype=np.float32)
    boxIndex=  np.array([0,1,3,2,3,2],dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)
    VBO,EBO = glGenBuffers(2)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 8, ctypes.c_void_p(0))
    

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, boxIndex.nbytes, boxIndex, GL_STATIC_DRAW)

    shaderProgram = createShader("shaders/vertex.txt", "shaders/fragment.txt")
    glUseProgram(shaderProgram)
    Tloc = glGetUniformLocation(shaderProgram, "rand")
    glUniform2fv(Tloc,1,[0,1])
    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)




def createShader(vertexFilepath: str, fragmentFilepath: str) -> int:
    with open(vertexFilepath,'r') as f:
        vertex_src = f.readlines()

    with open(fragmentFilepath,'r') as f:
        fragment_src = f.readlines()
    
    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                            compileShader(fragment_src, GL_FRAGMENT_SHADER))
    
    return shader

 
def render(fun = None):
    global shaderProgram
    global VAO
    glClearColor(0, 0, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shaderProgram)
    if fun != None:
        fun()

    glBindVertexArray(VAO)
    glDrawElements(GL_TRIANGLE_FAN, 4, GL_UNSIGNED_INT,None)
    

def createTexture(path, color=None):
    im = Image.open(path).transpose( Image.FLIP_TOP_BOTTOM )
    w,h = im.size
    if color != None:
        c = Image.new("RGBA",[w,h],color)
        im =ImageChops.multiply(im,c)
    imdata = bytes(im.convert("RGBA").tobytes())


    texname = glGenTextures(1)

    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glBindTexture(GL_TEXTURE_2D, texname)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0,
    GL_RGBA, GL_UNSIGNED_BYTE, imdata)
    glGenerateMipmap(GL_TEXTURE_2D)

    return texname


def main(fun):
    if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
        print(sdl2.SDL_GetError())
        return 
    window = sdl2.SDL_CreateWindow(b"rock",
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED, WIDTH, HIGHT,
                                   sdl2.SDL_WINDOW_OPENGL)
    if not window:
        print(sdl2.SDL_GetError())
        return
    
    sdl2.video.SDL_GL_SetAttribute(sdl2.video.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
    sdl2.video.SDL_GL_SetAttribute(sdl2.video.SDL_GL_CONTEXT_MINOR_VERSION, 3)
    sdl2.video.SDL_GL_SetAttribute(sdl2.video.SDL_GL_CONTEXT_PROFILE_MASK,
        sdl2.video.SDL_GL_CONTEXT_PROFILE_CORE)
    context = sdl2.SDL_GL_CreateContext(window)

    event = sdl2.SDL_Event()
    running = True

    init()
    render()
    sdl2.SDL_GL_SwapWindow(window)
    render()

    while running:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                running = False

        sdl2.SDL_GL_SwapWindow(window)
        sdl2.SDL_Delay(10)
        

    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()

if __name__ == "__main__":
    main()



