<!DOCTYPE html>
<html>
<head>
    <title>Simple PHP Form</title>
</head>
<body>
    <h1>Contact Us</h1>

    <?php
    // Initialize variables to store user input
    $name = "";
    $message = "";

    // Check if the form has been submitted
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Retrieve user input from the form
        $name = $_POST['name'];
        $message = $_POST['message'];

        // Process the data (you can save it to a file, send an email, or store it in a database)
        // For this example, we'll just display the submitted data
        echo "<h2>Thank you for your message, $name!</h2>";
        echo "<p>Your message: $message</p>";
    }
    ?>

    <!-- Simple PHP Form -->
    <form method="post">
        <label for="name">Your Name:</label>
        <input type="text" name="name" id="name" value="<?php echo $name; ?>" required>
        <br>
        <label for="message">Message:</label>
        <textarea name="message" id="message" rows="4" required><?php echo $message; ?></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
