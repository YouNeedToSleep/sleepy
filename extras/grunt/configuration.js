var
	jsGruntfile = 'Gruntfile',
	jsGrunttasks = 'extras/grunt/**/*.js',
	jsSource = 'src/sleepy/static/js/src/',
	jsSources = jsSource + '**/*.js',
	jsTemplates = 'src/sleepy/static/js/src/**/*.html',
	jsBuild = 'src/sleepy/static/js/build/',
	sassSources = 'src/config/static/scss/**/*.scss'
;

module.exports = {
	js: {
		gruntfile: jsGruntfile,
		grunttasks: jsGrunttasks,
		sourceDir: jsSource,
		sources: jsSources,
		buildDir: jsBuild,
		templates: jsTemplates,
	},

	sass: {
		sources: sassSources
	},
};
