import cv2
from ultralytics import YOLO

model = YOLO('yolo11n.pt')
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = frame.copy()

    for box in results[0].boxes:
        cls = int(box.cls[0])
        if cls == 0:  # Classe 0 = personne
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Exemple de critère : si la boîte est très grande, on dit "suspecte"
            area = (x2 - x1) * (y2 - y1)
            if area > 50000:  # Seuil arbitraire à ajuster
                label = "Personne suspecte"
                color = (0, 0, 255)
            else:
                label = "Personne non suspecte"
                color = (0, 255, 0)
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(annotated_frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('Détection de personne suspecte', annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()