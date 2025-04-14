setup:
	rye sync
	
run:
	rye run uvicorn src.main:app --reload

test:
	rye run pytest ./src/tests
