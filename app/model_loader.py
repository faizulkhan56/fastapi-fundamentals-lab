"""
ML Model Loader Module

This module handles loading and managing ML models for prediction endpoints.
The model is loaded once at application startup for optimal performance.
"""
import os
import joblib
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Global variable to store the loaded model
_ml_model: Optional[object] = None


def load_model(model_path: str = "models/model.pkl") -> Optional[object]:
    """
    Load the ML model from disk.
    
    Args:
        model_path: Path to the model file (default: "models/model.pkl")
    
    Returns:
        Loaded model object or None if loading fails
    """
    global _ml_model
    
    try:
        if not os.path.exists(model_path):
            logger.warning(f"Model file not found at {model_path}. Creating a default model...")
            # Create models directory if it doesn't exist
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            # Generate a default model
            try:
                from .train_model import create_default_model
                create_default_model(model_path)
            except ImportError:
                logger.error("train_model module not available. Cannot create default model.")
                return None
        
        _ml_model = joblib.load(model_path)
        logger.info(f"ML model loaded successfully from {model_path}")
        return _ml_model
    except Exception as e:
        logger.error(f"Error loading ML model: {str(e)}")
        # Create a default model as fallback
        try:
            from .train_model import create_default_model
            create_default_model(model_path)
            _ml_model = joblib.load(model_path)
            logger.info(f"Default model created and loaded from {model_path}")
            return _ml_model
        except Exception as fallback_error:
            logger.error(f"Failed to create default model: {str(fallback_error)}")
            return None


def get_model() -> Optional[object]:
    """
    Get the loaded ML model.
    
    Returns:
        The loaded model object or None if not loaded
    """
    return _ml_model


def predict(features: list) -> float:
    """
    Make a prediction using the loaded model.
    
    Args:
        features: List of feature values [feature1, feature2, feature3]
    
    Returns:
        Prediction value as float
    
    Raises:
        ValueError: If model is not loaded or prediction fails
    """
    global _ml_model
    
    if _ml_model is None:
        raise ValueError("ML model is not loaded. Please ensure the model is loaded at startup.")
    
    try:
        # Reshape features for model input (assuming sklearn model)
        import numpy as np
        features_array = np.array(features).reshape(1, -1)
        prediction = _ml_model.predict(features_array)
        return float(prediction[0])
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        raise ValueError(f"Prediction failed: {str(e)}")

