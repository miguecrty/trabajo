const http = require('http');
const express = require('express');
const cors = require('cors'); // Importa el módulo cors
const { Pool } = require('pg');
const app = express();

// Utiliza el middleware cors
app.use(cors());
const pool = new Pool({
  user: 'postgres',
  host: '10.0.0.3',
  database: 'sta',
  password: 'clave',
  port: 5000,
});
function conexion()
{

pool.connect((err, client, release) => {
  if (err) {
    conexion();
  }
});

pool.on('error', (err) => {
  console.error('Error en la conexión a PostgreSQL:');
	conexion();
});

}

conexion();
console.log('Conexión exitosa a PostgreSQL');
app.get('/api', (req, res) => {
  const nombre = req.query.nombre;
  const edad = req.query.edad;

  console.log('Ha registrado en la BBDD el nombre: ' + nombre + ' y la edad: ' + edad);

  // Consulta SQL para insertar los datos en la tabla 'datos'
  const query = 'INSERT INTO datos (nombre, edad) VALUES ($1, $2) RETURNING id';

  // Parámetros para la consulta SQL
  const values = [nombre, edad];

  // Ejecutar la consulta SQL
  pool.query(query, values, (err, result) => {
    if (err) {
      console.error('Error al insertar datos');
      res.status(500).json({ error: 'Error al insertar datos en la base de datos' });
    } else {
      // Obtener el ID generado por la base de datos
      const insertedId = result.rows[0].id;
      // Responder con el ID generado
      res.json({ id: insertedId });
    }
  });
});

app.get('/lista', (req, res) => {
  pool.query('SELECT * FROM datos', (error, results) => {
    if (error) {
      throw error;
    }
    res.send(results.rows);
  });
});
app.get('/borrar', (req, res) => {
  console.log('Se ha borrado la lista');
  const deleteQuery = 'DELETE FROM datos';
  pool.query(deleteQuery, (err, result) => {
    if (err) {
      console.error('Error al borrar datos');
      res.status(500).json({ error: 'Error al borrar los datos de la base de datos', resultado: 'error' });
    } else {
		  const resetSequenceQuery = 'SELECT setval(\'datos_id_seq\', 1, false)';
		  pool.query(resetSequenceQuery, (error, results) => {
		    if (error) {
		      console.error('Error al reiniciar la secuencia');
		      res.status(500).json({ error: 'Error al reiniciar la secuencia', resultado: 'error' });
		    } else {
		      console.log('Éxito al borrar y reiniciar la secuencia');
		      res.json({ resultado: 'exito' });
		    }
		  });
    }
  });
});

process.on('uncaughtException', (err) => {
  console.error('BBDD caída reintentando conexion');
	conexion();
  // Puedes tomar medidas adicionales aquí si es necesario
});

const server = http.createServer(app);

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
