import Publicacion.Autor;
import Publicacion.Libro;

public class Main {
    public static void main(String[] args) {
        Autor autor = new Autor("Jose Manrin", "Ostras Pedrin", "Lucas Balmaceda",);
        Libro libro = new Libro("Hola", "10/02/3200", "leolas", autor, "29852314", 200, 10, "Literatura", Genero.LITERATURA);
        System.out.println(libro);
    }
}