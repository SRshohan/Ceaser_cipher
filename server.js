const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: "1srtechzone@gmail.com",
    pass: "fxedvqiraihwtrpd"
  }
});

function sendEmail(email, subject, message) {
  const mailOptions = {
    from: "your-email@gmail.com",
    to: email,
    subject: subject,
    text: message
  };

  transporter.sendMail(mailOptions, function(error, info) {
    if (error) {
      console.log(error);
    } else {
      console.log("Email sent: " + info.response);
    }
  });
}

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static(__dirname + "/public"));

app.get("/", function(req, res) {
  res.send(`
    <html>
      <head>
        <title>Send Email</title>
        <style>
          form {
            width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            text-align: center;
          }
          input[type="text"],
          input[type="email"],
          textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
          }
          input[type="submit"] {
            padding: 10px 20px;
            border: none;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            cursor: pointer;
          }
          input[type="submit"]:hover {
            background-color: #3e8e41;
          }
        </style>
      </head>
      <body>
        <form action="/send-email" method="post">
          <input type="email" name="email" placeholder="Email" required>
          <input type="text" name="subject" placeholder="Subject" required>
          <textarea name="message" rows="10" placeholder="Message" required></textarea>
          <input type="submit" value="Send">
        </form>
      </body>
    </html>
  `);
});

app.post("/send-email", function(req, res) {
  const email = req.body.email;
  const subject = req.body.subject;
  const message = req.body.message;

  if (!email || !subject || !message) {
    return res.status(400).send({ error: "All fields are required." });
  }

  sendEmail(email, subject, message);

  res.send("Email sent!");
});
