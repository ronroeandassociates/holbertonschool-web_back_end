// Link the route / to the AppController
// Link the route /students and /students/:major
// to the StudentsController

import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const express = require('express');

const router = express.Router();

router.get('/students/:major', StudentsController.getAllStudentsByMajor);
router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getStudents);

module.exports = router;
