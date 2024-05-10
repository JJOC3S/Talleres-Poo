package Estante;

public class Estante {
    private int numeroLibros;

    private Sector sector;

    public Estante(int numeroLibros, Sector sector) {
        this.numeroLibros = numeroLibros;
        this.sector = sector;
    }

    public int getNumeroLibros() {
        return numeroLibros;
    }

    public void setNumeroLibros(int numeroLibros) {
        this.numeroLibros = numeroLibros;
    }
}
