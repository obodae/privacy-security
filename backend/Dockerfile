# Dockerfile for Backend

# Base image
FROM node:14

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json for installing dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD [ "npm", "start" ]