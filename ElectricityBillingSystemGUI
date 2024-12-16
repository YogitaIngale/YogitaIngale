import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

class Consumer {
    private int id;
    private String name;
    private String address;
    private String type; // e.g., Residential, Commercial
    private double unitsConsumed;

    public Consumer(int id, String name, String address, String type, double unitsConsumed) {
        this.id = id;
        this.name = name;
        this.address = address;
        this.type = type;
        this.unitsConsumed = unitsConsumed;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public String getAddress() { return address; }
    public String getType() { return type; }
    public double getUnitsConsumed() { return unitsConsumed; }
}

class Bill {
    public static double calculateBill(String type, double units) {
        double rate;
        switch (type.toLowerCase()) {
            case "residential":
                rate = units <= 100 ? 1.5 : units <= 300 ? 2.0 : 3.0;
                break;
            case "commercial":
                rate = units <= 100 ? 2.5 : units <= 300 ? 3.0 : 5.0;
                break;
            default: // Industrial
                rate = units <= 100 ? 3.5 : units <= 300 ? 4.0 : 6.0;
                break;
        }
        return units * rate;
    }
}

public class ElectricityBillingSystemGUI extends JFrame {
    private ArrayList<Consumer> consumers = new ArrayList<>();
    private JTextArea outputArea;

    public ElectricityBillingSystemGUI() {
        setTitle("Electricity Billing System");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Output Area
        outputArea = new JTextArea();
        outputArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(outputArea);
        add(scrollPane, BorderLayout.CENTER);

        // Buttons
        JPanel buttonPanel = new JPanel();
        JButton addConsumerButton = new JButton("Add Consumer");
        JButton generateBillButton = new JButton("Generate Bill");
        JButton exitButton = new JButton("Exit");

        buttonPanel.add(addConsumerButton);
        buttonPanel.add(generateBillButton);
        buttonPanel.add(exitButton);
        add(buttonPanel, BorderLayout.SOUTH);

        // Button Actions
        addConsumerButton.addActionListener(e -> addConsumer());
        generateBillButton.addActionListener(e -> generateBill());
        exitButton.addActionListener(e -> System.exit(0));
    }

    private void addConsumer() {
        JTextField idField = new JTextField();
        JTextField nameField = new JTextField();
        JTextField addressField = new JTextField();
        JComboBox<String> typeBox = new JComboBox<>(new String[]{"Residential", "Commercial", "Industrial"});
        JTextField unitsField = new JTextField();

        JPanel panel = new JPanel(new GridLayout(5, 2));
        panel.add(new JLabel("Consumer ID:"));
        panel.add(idField);
        panel.add(new JLabel("Name:"));
        panel.add(nameField);
        panel.add(new JLabel("Address:"));
        panel.add(addressField);
        panel.add(new JLabel("Type:"));
        panel.add(typeBox);
        panel.add(new JLabel("Units Consumed:"));
        panel.add(unitsField);

        int result = JOptionPane.showConfirmDialog(this, panel, "Add Consumer", JOptionPane.OK_CANCEL_OPTION);
        if (result == JOptionPane.OK_OPTION) {
            try {
                int id = Integer.parseInt(idField.getText());
                String name = nameField.getText();
                String address = addressField.getText();
                String type = (String) typeBox.getSelectedItem();
                double units = Double.parseDouble(unitsField.getText());

                consumers.add(new Consumer(id, name, address, type, units));
                outputArea.append("Consumer added successfully!\n");
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Invalid input! Please try again.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    private void generateBill() {
        String inputId = JOptionPane.showInputDialog(this, "Enter Consumer ID:");
        if (inputId != null) {
            try {
                int id = Integer.parseInt(inputId);

                for (Consumer consumer : consumers) {
                    if (consumer.getId() == id) {
                        double amount = Bill.calculateBill(consumer.getType(), consumer.getUnitsConsumed());
                        outputArea.append("\n--- Bill Details ---\n");
                        outputArea.append("Name: " + consumer.getName() + "\n");
                        outputArea.append("Address: " + consumer.getAddress() + "\n");
                        outputArea.append("Type: " + consumer.getType() + "\n");
                        outputArea.append("Units Consumed: " + consumer.getUnitsConsumed() + "\n");
                        outputArea.append("Total Bill: $" + amount + "\n");
                        return;
                    }
                }
                JOptionPane.showMessageDialog(this, "Consumer not found!", "Error", JOptionPane.ERROR_MESSAGE);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Invalid ID! Please enter a valid number.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            ElectricityBillingSystemGUI frame = new ElectricityBillingSystemGUI();
            frame.setVisible(true);
        });
    }
}
