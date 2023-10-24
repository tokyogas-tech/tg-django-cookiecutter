import gulp from 'gulp';
import autoprefixer from 'gulp-autoprefixer';
import browserSyncModule from 'browser-sync';
const browserSync = browserSyncModule.create();
import cleanCss from 'gulp-clean-css';
import gulpSass from 'gulp-sass';
import * as sassModule from 'sass';
const sass = gulpSass(sassModule);
import wait from 'gulp-wait';
import sourcemaps from 'gulp-sourcemaps';
import rename from 'gulp-rename';

// Define COMMON paths

const paths = {
    src: {
        base: './static',
        css: './static/css',
        scss: './assets/scss',
        node_modules: './node_modules/',
        vendor: './vendor'
    }
};

// Compile SCSS
function scss() {
    return gulp.src([paths.src.scss + '/dashboard.scss'])
        .pipe(wait(500))
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer('last 2 versions'))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(paths.src.css))
        .pipe(browserSync.stream());
}

// Minify CSS
function minify() {
    return gulp.src([paths.src.css + '/dashboard.css'])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = '.min.css';
        }))
        .pipe(gulp.dest(paths.src.css));
}

gulp.task('scss:watch', function() {
    gulp.watch([paths.src.scss + '/**/*.scss'], scss);
    gulp.watch([paths.src.css + '/**/*.css', '!' + paths.src.css + '/**/*.min.css'], minify);
});

// Default Task: Compile SCSS and minify the result
gulp.task('default', gulp.series('scss:watch'));
