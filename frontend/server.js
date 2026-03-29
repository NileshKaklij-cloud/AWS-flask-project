const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.send(`
    <h2>To-Do Form</h2>
    <form method="POST" action="http://13.232.89.67:5000/submittodoitem"> 
      <input name="itemName" placeholder="Item Name"/><br/><br/>
      <textarea name="itemDescription" placeholder="Item Description"></textarea><br/><br/>
      <button type="submit">Submit</button>
    </form>
  `);
});

app.listen(3000, "0.0.0.0", () => {
  console.log("Frontend running on port 3000");
});
