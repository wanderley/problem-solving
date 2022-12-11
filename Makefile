.PHONY = site iterate-site clean

SOURCE_DIR = notes
BUILD_DIR  = out

site:
	@emacs --batch -l build.el -f "wander/publish-site" --kill

iterate-site:
	@emacs --batch -l build.el -f "wander/iterate-site" --kill

clean:
	rm -rf $BUILD_DIR
