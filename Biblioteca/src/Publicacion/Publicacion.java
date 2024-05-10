package Publicacion;

public abstract class Publicacion {
    protected String titulo;
    protected String fechaLanzamiento;
    protected Autor autor;

    public Publicacion(String titulo, String fechaLanzamiento, Autor autor) {
        this.titulo = titulo;
        this.fechaLanzamiento = fechaLanzamiento;
        this.autor = autor;
    }

    public Autor getAutor() {
        return autor;
    }

    public void setAutor(Autor autor) {
        this.autor = autor;
    }
}
