# My Project

This project is structured into three main parts: the frontend, backend, and AI models. 

## Frontend

The frontend is built using React and Next.js. It includes reusable components, page components for routing, and styles for the application.

- **Components**: Located in `frontend/src/components`, this directory contains reusable React components.
- **Pages**: Located in `frontend/src/pages`, this directory contains the main entry points for routing in the Next.js application.
- **Styles**: Located in `frontend/src/styles`, this directory contains CSS or styled-components for styling the React components.
- **Static Assets**: Located in `frontend/public`, this directory contains static assets such as images and fonts.

## Backend

The backend is built using Next.js and provides API routes for server-side functionality.

- **API Routes**: Located in `backend/pages/api`, this directory contains the API route handlers.
- **Configuration**: The `backend/next.config.js` file allows customization of the build and server behavior.

## AI Models

The AI models are implemented using PyTorch and include scripts for data preprocessing, training, and prediction.

- **Scripts**: Located in `ai_models/scripts`, this directory contains scripts for preprocessing data, training models, and making predictions.
- **Model Weights**: The trained model weights are stored in `ai_models/models/model.pth`.

## Getting Started

To get started with this project, clone the repository and install the necessary dependencies for both the frontend and backend. Follow the instructions in the respective `README.md` files for detailed setup and usage information.