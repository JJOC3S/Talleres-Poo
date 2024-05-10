package Publicacion;

public class Libro {
    private String isbn;
    private int paginas;

    public Genero genero;

    public Book(String titulo, String fechaLanzamiento, String editorial, Autor autor, String isbn, int paginas, Genero genero) {
        super();
        this.isbn = isbn;
        this.paginas = paginas;
        this.genero = genero;
    }

    public Genero getGenero() {
        return genero;
    }

    public void setGenero(Genero genero) {
        this.genero = genero;
    }

    public int getpaginas() {
        return paginas;
    }

    public void setpaginas(int paginas) {
        this.paginas = paginas;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
}
