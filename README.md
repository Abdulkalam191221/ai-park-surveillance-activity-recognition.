# AI-Based Intelligent Video Surveillance Platform for Activity Recognition and Security Management in Parks

## 📌 Project Overview
Developed during the Infosys Springboard Virtual Internship 6.0 (Batch 13), this project is an AI-powered intelligent video surveillance system designed to enhance safety and security in public park environments. The platform processes video streams in real time to detect, classify, and monitor human activities, distinguishing between authorized behaviors (e.g., walking, running, yoga, meditation) and unauthorized or unsafe actions.

### 🔑 Key Metrics & Capabilities
* **Real-Time Processing:** Low-latency inference optimized at **14ms**.
* **High Accuracy:** Achieved a **98.4%** accuracy rate under optimized conditions.
* **Continuous Monitoring:** Engineered for **24/7** automated surveillance execution to minimize manual security oversight.

---

## 🛠️ System Architecture & Pipeline
The system utilizes a hybrid AI pipeline combining deep learning-based object detection and human pose estimation:

1.  **Video Input:** Processes video streams frame-by-frame through the pipeline.
2.  **Unsafe Object Check:** Scans frames for predefined unsafe objects (e.g., unauthorized vehicles like motorcycles inside pedestrian zones, weapons, or hazards). If flagged above a 10% frame threshold, the video is instantly marked **UNSAFE**.
3.  **Pose Estimation:** Extracts key body landmarks and calculates joint angles from the human subjects in the frame.
4.  **Activity Classification:** Feeds joint angles into a trained classifier to identify the specific activity (e.g., Walking, Sitting, Running, Yoga/Meditation).
5.  **Final Verdict:** Generates a real-time visual overlay showing a `SAFE` or `UNSAFE` status along with a confidence score.

---

## 💻 Tech Stack & Tools
* **Programming Language:** Python
* **Core Frameworks:** Computer Vision, Machine Learning, Deep Learning
* **Models Implemented:** YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector)
* **Techniques:** Frame Extraction, Noise Reduction, Image Resizing, Normalization, Data Annotation, Hyperparameter Tuning
* **UI Framework:** Web-based interface integrating Model Inference, Prediction Logs, and Analytics History.

---

## 📅 Project Timeline & Milestones
* **Week 1–2:** Data Collection & Annotation (Structuring training/testing datasets for park scenarios).
* **Week 3–4:** Preprocessing & Model Selection (Applying noise reduction and initializing YOLO/SSD training).
* **Week 5–6:** Model Evaluation & UI Integration (Parameter fine-tuning and building the real-time web dashboard).
* **Week 7–8:** System Validation & Optimization (Debugging latency issues, resolving misclassifications, and final documentation).

---

## 🚀 Challenges Overcome
1.  **Environmental Data Inconsistencies:** Handled real-world video challenges like varying lighting conditions, background noise, and shadows by implementing robust preprocessing (normalization and frame resizing).
2.  **Activity Misclassification:** Mitigated initial overlap issues between similar human actions through rigorous iterative training and hyperparameter tuning to secure reliable boundaries between classes.
3.  **Real-Time Constraints:** Optimized model responsiveness and inference speeds to achieve smooth, real-time live video processing.

---

## 👥 Acknowledgements
* **Organization:** Infosys Springboard Internship Team
* **Mentor:** Bhargava Sai Reddy Vanga
* **Coordinator:** Pranathi MDM
