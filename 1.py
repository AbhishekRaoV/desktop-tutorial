
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const mysql = require('mysql');
const cors = require('cors');
const path = require('path');

const app = express();
const port = 3001;

app.use(cors());

const jenkinsProxy = createProxyMiddleware({
  target: 'http://10.63.20.41:8080',
  changeOrigin: true,
  pathRewrite: {
      '^/jenkinsProxy': '/view/sustainability/job/sustain/buildWithParameters'
  }
});

// Use the Jenkins proxy middleware
app.use('/jenkinsProxy', jenkinsProxy);

const connection = mysql.createConnection({
  host: '10.63.14.112',
  user: 'root',
  password: 'admin',
  database: 'mysql'
});

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE', 'UPDATE');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

connection.connect();

// Route to fetch progress level
app.get('/', (req, res) => {
  const query = "SELECT COUNT(CASE WHEN Status = 'Yes' THEN 1 END) AS progressLevel FROM GreenTechLevels";
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).send('Error fetching progress level');
    } else {
      res.send(results[0].progressLevel.toString());
      console.log(results[0].progressLevel.toString());
    }
  });
});
app.get('/levels2', (req, res) => {
  const query = "SELECT COUNT(CASE WHEN Status = 'Yes' THEN 1 END) AS progressLevel FROM GreenTechLevels2";
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).send('Error fetching progress level');
    } else {
      res.send(results[0].progressLevel.toString());
      console.log(results[0].progressLevel.toString());
    }
  });
});

// Route to handle query for implemented = 'yes'
app.get('/implemented_yes', (req, res) => {
  const query = "SELECT * FROM sustainability_actions WHERE implemented = 'yes'";
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).send('Error fetching data');
    } else {
      res.json(results);
    }
  });
});

// Route to handle query for implemented = 'no'
app.get('/implemented_no', (req, res) => {
  const query = "SELECT * FROM sustainability_actions WHERE implemented = 'no'";
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).send('Error fetching data');
    } else {
      res.json(results);
    }
  });
});
app.get('/implemented_yes2', (req, res) => {
  const query = "SELECT * FROM sustainability_actions2 WHERE implemented = 'yes'";
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).send('Error fetching data');
    } else {
      res.json(results);
    }
  });
});

// Route to handle query for implemented = 'no'
app.get('/implemented_no2', (req, res) => {
  const query = "SELECT * FROM sustainability_actions2 WHERE implemented = 'no'";
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).send('Error fetching data');
    } else {
      res.json(results);
    }
  });
});

// instance details
app.get('/instances', (req, res) => {
  // Query MySQL database
  connection.query('SELECT instanceName, instanceId, InstanceType, InstanceState, cpuUtilization, energy, region, suggested_instance FROM Metric', (error, results, fields) => {
    if (error) {
      console.error('Error querying database:', error);
      res.status(500).send('Internal Server Error');
      return;
    }
    // Send JSON response with data
    res.json(results);
  });
});
app.get('/unused', (req, res) => {
  // Query MySQL database
  connection.query("SELECT instanceId, instanceName, instanceState, instanceType, DATE_FORMAT(STR_TO_DATE(startTime, '%d %b %Y'), '%d-%m-%Y') AS startTimeConverted, TIMESTAMPDIFF(DAY, STR_TO_DATE(startTime, '%d %b %Y %H:%i:%s GMT'), NOW()) AS 'Unused Days' FROM mysql.Metric WHERE TIMESTAMPDIFF(DAY, STR_TO_DATE(startTime, '%d %b %Y %H:%i:%s GMT'), NOW()) > 7 AND instanceState = 'stopped';  ", (error, results, fields) => {
    if (error) {
      console.error('Error querying database:', error);
      res.status(500).send('Internal Server Error');
      return;
    }
    // Send JSON response with data
    res.json(results);
  });
});
app.get('/low_cpu', (req, res) => {
  // Query MySQL database
  connection.query("select instanceName, instanceId, instanceState, cpuUtilization, instanceType, suggested_instance FROM Metric WHERE cpuUtilization IS NOT NULL   ORDER BY cpuUtilization ASC LIMIT 5;", (error, results, fields) => {
    if (error) {
      console.error('Error querying database:', error);
      res.status(500).send('Internal Server Error');
      return;
    }
    // Send JSON response with data
    res.json(results);
  });
});
app.get('/high_cpu', (req, res) => {
  // Query MySQL database
  connection.query("select instanceName, instanceId, instanceState, cpuUtilization, instanceType, suggested_instance FROM Metric WHERE cpuUtilization IS NOT NULL   ORDER BY cpuUtilization DESC LIMIT 5;", (error, results, fields) => {
    if (error) {
      console.error('Error querying database:', error);
      res.status(500).send('Internal Server Error');
      return;
    }
    // Send JSON response with data
    res.json(results);
  });
});

// Serve index.html
app.use(express.static(__dirname));

// Route to serve index.html explicitly
app.get('/index', (req, res) => {
  res.sendFile(path.join(__dirname, '/index_with_changes.html'));
});
app.get('/ec2', (req, res) => {
  res.sendFile(path.join(__dirname, '/ec2.html'));
});
app.get('/unused_resources', (req, res) => {
  res.sendFile(path.join(__dirname, '/unused.html'));
});
app.get('/llm', (req, res) => {
  res.sendFile(path.join(__dirname, '/EnergyMetrics.mp4'));
});
app.get('/lambda', (req, res) => {
  res.sendFile(path.join(__dirname, '/Lamdba-func.mp4'));
});

app.get('/energy_usage', (req, res) => {
  res.sendFile(path.join(__dirname, '/energy-usage-report.pdf'));
});
app.get('/jenkins', (req, res) => {
  res.sendFile(path.join(__dirname, '/form.html'));
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
