module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		sass: {
			options: {
				includePaths: ['bower_components/foundation/scss'],
			},
			dist: {
				options: {
					outputStyle: "expanded"
				},
				files: {
					"src/sleepy/static/css/app.css": "src/sleepy/static/scss/app.scss"
				},
			}
		},
		watch: {
			options: {
				livereload: true
			},
			grunt: {
				files: ["Gruntfile.js"]
			},
			sass: {
				files: [
					"src/sleepy/static/scss/app.scss",
					"src/sleepy/static/scss/_settings.scss"
				],
				tasks: ["sass"],
			},
			html: {
				files: ['src/sleepy/templates/sleepy/web/*.html']
			}
		}
	});

	grunt.loadTasks('extras/grunt/tasks');

	grunt.loadNpmTasks("grunt-sass");
	grunt.loadNpmTasks("grunt-contrib-watch");
	grunt.registerTask("build", ["sass"]);

	grunt.registerTask(
		'default',
		'Run all tasks in a row.',
		['build']
	);

	grunt.registerTask(
		'validate',
		'Validate all files.',
		['jshint', 'jscs', 'lintspaces']
	);

	grunt.registerTask(
		'test',
		'Run JS tests.',
		[]
	);

	grunt.registerTask(
		'build',
		'Build all JS files for a deploy.',
		['validate', 'clean']
	);
};
