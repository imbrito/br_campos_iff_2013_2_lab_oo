deps: specloud should-dsl

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install specloud


should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/hugobr/should-dsl/tarball/master

path:
    export PYTHONPATH=..
	

teste:  specloud should-dsl
	@echo ============================================================
	@echo ========= Running Teste unit specs ==========
	@specloud  spec/
	@echo

all: teste
