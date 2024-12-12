
CREATE OR REPLACE FUNCTION manage_order_status()
RETURNS TRIGGER AS $$
DECLARE
    product_row RECORD;
BEGIN
   
    IF NEW.status = 'Pending' THEN
        
        FOR product_row IN
            SELECT po.product_id, po.quantity
            FROM "Product_Order" po
            WHERE po.order_id = NEW.order_id
        LOOP
            UPDATE "Product"
            SET quantity = quantity - product_row.quantity,
                reserved = COALESCE(reserved, 0) + product_row.quantity
            WHERE product_id = product_row.product_id;
        END LOOP;
    
    ELSIF NEW.status = 'Shipped' THEN
        
        FOR product_row IN
            SELECT po.product_id, po.quantity
            FROM "Product_Order" po
            WHERE po.order_id = NEW.order_id
        LOOP
            UPDATE "Product"
            SET reserved = reserved - product_row.quantity
            WHERE product_id = product_row.product_id;
        END LOOP;

    ELSIF NEW.status = 'Cancelled' THEN
        
        FOR product_row IN
            SELECT po.product_id, po.quantity
            FROM "Product_Order" po
            WHERE po.order_id = NEW.order_id
        LOOP
            UPDATE "Product"
            SET quantity = quantity + product_row.quantity,
                reserved = NULL
            WHERE product_id = product_row.product_id;
        END LOOP;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER manage_order_status
AFTER INSERT OR UPDATE OF status
ON "Delivery"
FOR EACH ROW
EXECUTE FUNCTION manage_order_status();

