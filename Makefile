setup:
	rye sync
	
run:
       PYTHONPATH=src uvicorn src.main:app --reload

test:
       PYTHONPATH=src pytest ./src/tests
