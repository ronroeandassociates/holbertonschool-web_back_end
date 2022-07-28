// Link the route / to the AppController
// Link the route /students and /students/:major
// to the StudentsController

import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const express = require('express');

const route = express.Route();

route.get('/students/:major', StudentsController.getAllStudentsByMajor);
route.get('/', AppController.getHomepage);
route.get('/students', StudentsController.getStudents);

module.exports = route;
