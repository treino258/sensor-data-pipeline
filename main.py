from sensor_pipeline.context import correlation_id_ctx
from sensor_pipeline.audit_logger import get_audit_logger
from sensor_pipeline.core.process import process_file
from sensor_pipeline.logger import get_logger
from sensor_pipeline.adapters.ml_adapter import to_ml_input
from sensor_pipeline.adapters.api_adapter import to_api_response
from sensor_pipeline.adapters.storage_adapter import to_storage_records
from uuid import uuid4

logger = get_logger(__name__)
audit = get_audit_logger()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    # gerar correlation_id e setar no contexto 
    cid = uuid4().hex
    correlation_id_ctx.set(cid)

    # audit = evento de alto nível
    audit.info(f"Pipeline iniciado")

    logger.info("Starting pipeline via main")            # fluxo normal
    result = process_file(args.file)                    # process_file faz logs INFO
    
    
    

    ml_data = to_ml_input(result)
    api_data = to_api_response(result)
    storage_data = to_storage_records(
        result,
        correlation_id_ctx.get()
    )
    
    
    logger.info("Done")                             # fluxo normal

    audit.info("Pipeline finalizado")
    


# python -m main --file sample_data/sensor.txt    para rodar o pipeline