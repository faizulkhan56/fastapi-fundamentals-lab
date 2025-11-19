"""
ML Model Training Script

This script creates and trains a simple ML model for demonstration purposes.
In production, you would train your model separately and save it.
"""
import os
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import logging

logger = logging.getLogger(__name__)


def create_default_model(model_path: str = "models/model.pkl"):
    """
    Create a simple default ML model for demonstration.
    
    This function creates a Linear Regression model trained on synthetic data.
    In a real scenario, you would train your model with actual data.
    
    Args:
        model_path: Path where the model will be saved
    """
    try:
        # Create models directory if it doesn't exist
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Generate synthetic training data
        # In production, you would load real data here
        np.random.seed(42)
        n_samples = 1000
        
        # Generate features
        X = np.random.rand(n_samples, 3) * 10  # 3 features, values 0-10
        
        # Generate target (simple linear relationship with some noise)
        y = 2 * X[:, 0] + 1.5 * X[:, 1] + 0.5 * X[:, 2] + np.random.randn(n_samples) * 0.5
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Evaluate model (optional, for logging)
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        logger.info(f"Model trained - Train R²: {train_score:.4f}, Test R²: {test_score:.4f}")
        
        # Save model
        joblib.dump(model, model_path)
        logger.info(f"Model saved to {model_path}")
        
        return model
    except Exception as e:
        logger.error(f"Error creating default model: {str(e)}")
        raise


if __name__ == "__main__":
    # Run this script to generate the model
    model_path = "models/model.pkl"
    create_default_model(model_path)
    print(f"Model created and saved to {model_path}")

