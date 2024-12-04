CREATE OR REPLACE FUNCTION log_delivery_update()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.status = 'Pending' THEN
        INSERT INTO "Event" (event_id, message)
        VALUES (
            (SELECT nextval('event_event_id_seq')), 
            'Change status order ' || OLD.order_id || ' to new status ' || NEW.status
        );
    ELSE
      INSERT INTO "Event" (event_id, message)
        VALUES (
          (SELECT nextval('event_event_id_seq')), 
            'Change status order ' || OLD.order_id || ' Unknown ' || NEW.status
        );
    END IF;
    RETURN NEW; 
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER UpdateTrigger
AFTER UPDATE ON "Delivery" 
FOR EACH ROW
EXECUTE FUNCTION log_delivery_update();