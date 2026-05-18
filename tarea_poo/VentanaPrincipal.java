 

import javax.swing.*;
import java.awt.event.*;

public class VentanaPrincipal extends JFrame implements ActionListener {
    
    // Declaración de componentes
    JLabel lblNota1, lblNota2, lblNota3, lblNota4, lblNota5;
    JTextField txtNota1, txtNota2, txtNota3, txtNota4, txtNota5;
    JButton btnCalcular, btnLimpiar;
    JLabel lblPromedio, lblDesviacion, lblMayor, lblMenor;

    public VentanaPrincipal() {
        // Configuración de la ventana
        setTitle("Cálculo de Notas");
        setSize(350, 420);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null); // Uso de layout absoluto para posicionamiento manual

        // Inicialización y ubicación de etiquetas y campos de texto
        lblNota1 = new JLabel("Nota 1:");
        lblNota1.setBounds(30, 20, 80, 25);
        add(lblNota1);
        txtNota1 = new JTextField();
        txtNota1.setBounds(120, 20, 150, 25);
        add(txtNota1);

        lblNota2 = new JLabel("Nota 2:");
        lblNota2.setBounds(30, 50, 80, 25);
        add(lblNota2);
        txtNota2 = new JTextField();
        txtNota2.setBounds(120, 50, 150, 25);
        add(txtNota2);

        lblNota3 = new JLabel("Nota 3:");
        lblNota3.setBounds(30, 80, 80, 25);
        add(lblNota3);
        txtNota3 = new JTextField();
        txtNota3.setBounds(120, 80, 150, 25);
        add(txtNota3);

        lblNota4 = new JLabel("Nota 4:");
        lblNota4.setBounds(30, 110, 80, 25);
        add(lblNota4);
        txtNota4 = new JTextField();
        txtNota4.setBounds(120, 110, 150, 25);
        add(txtNota4);

        lblNota5 = new JLabel("Nota 5:");
        lblNota5.setBounds(30, 140, 80, 25);
        add(lblNota5);
        txtNota5 = new JTextField();
        txtNota5.setBounds(120, 140, 150, 25);
        add(txtNota5);

        // Botones
        btnCalcular = new JButton("Calcular");
        btnCalcular.setBounds(50, 190, 100, 30);
        btnCalcular.addActionListener(this);
        add(btnCalcular);

        btnLimpiar = new JButton("Limpiar");
        btnLimpiar.setBounds(180, 190, 100, 30);
        btnLimpiar.addActionListener(this);
        add(btnLimpiar);

        // Etiquetas de resultados
        lblPromedio = new JLabel("Promedio:");
        lblPromedio.setBounds(30, 240, 280, 25);
        add(lblPromedio);

        lblDesviacion = new JLabel("Desviación estándar:");
        lblDesviacion.setBounds(30, 270, 280, 25);
        add(lblDesviacion);

        lblMayor = new JLabel("Mayor nota obtenida:");
        lblMayor.setBounds(30, 300, 280, 25);
        add(lblMayor);

        lblMenor = new JLabel("Menor nota obtenida:");
        lblMenor.setBounds(30, 330, 280, 25);
        add(lblMenor);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnCalcular) {
            Notas misNotas = new Notas();
            
            // Se asignan los valores directamente parseando el texto a double
            misNotas.listaNotas[0] = Double.parseDouble(txtNota1.getText());
            misNotas.listaNotas[1] = Double.parseDouble(txtNota2.getText());
            misNotas.listaNotas[2] = Double.parseDouble(txtNota3.getText());
            misNotas.listaNotas[3] = Double.parseDouble(txtNota4.getText());
            misNotas.listaNotas[4] = Double.parseDouble(txtNota5.getText());

            // Se muestran los resultados formateados
            lblPromedio.setText("Promedio: " + String.format("%.2f", misNotas.calcularPromedio()));
            lblDesviacion.setText("Desviación estándar: " + String.format("%.2f", misNotas.calcularDesviacion()));
            lblMayor.setText("Mayor nota obtenida: " + misNotas.calcularMayor());
            lblMenor.setText("Menor nota obtenida: " + misNotas.calcularMenor());
        }

        if (e.getSource() == btnLimpiar) {
            // Se vacían los campos de texto
            txtNota1.setText("");
            txtNota2.setText("");
            txtNota3.setText("");
            txtNota4.setText("");
            txtNota5.setText("");

            // Se reinician las etiquetas
            lblPromedio.setText("Promedio:");
            lblDesviacion.setText("Desviación estándar:");
            lblMayor.setText("Mayor nota obtenida:");
            lblMenor.setText("Menor nota obtenida:");
        }
    }

    public static void main(String[] args) {
        VentanaPrincipal miVentana = new VentanaPrincipal();
        miVentana.setVisible(true);
    }
}
