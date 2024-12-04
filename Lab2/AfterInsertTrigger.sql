CREATE OR REPLACE FUNCTION create_delivery()
RETURNS TRIGGER AS $$
DECLARE
    new_delivery_id INTEGER;
BEGIN
    INSERT INTO "Delivery" (delivery_id, address, status, order_id)
        VALUES ((SELECT nextval('delivery_delivery_id_seq') FROM generate_series(1,1)), 'Address TBD', 'Pending', NEW.order_id);
    RETURN NEW;
EXCEPTION
    WHEN OTHERS THEN
        RAISE WARNING 'Error in AfterInsertTrigger: %', SQLERRM;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER AfterInsertTrigger
AFTER INSERT ON "Order"
FOR EACH ROW
EXECUTE FUNCTION create_delivery();