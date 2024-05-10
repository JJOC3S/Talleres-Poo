package Estructura;

import java.util.ArrayList;

public class Sector {
    private int nombre;

    private ArrayList<Estante> estante;

    public Sector(int nombre) {
        this.nombre = nombre;
        this.estante = new ArrayList<>();
    }
    
    public int getNombre() {
        return nombre;
    }
}
