# Use the official Node.js image
FROM node:18-alpine as base

# Set the working directory
WORKDIR /app

# Copy the package.json, yarn.lock, package-lock.json, and pnpm-lock.yaml files into the container at /app
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./ 

# Checks for the presence of different lockfiles to determine the package manager to use for installing dependencies.
RUN \
    if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i --frozen-lockfile; \
    else echo "No lockfile found" && exit 1; \
    fi

# Copy the content of the local src directory to the working directory
COPY . .

# Build the application
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000 

# Run the Application
CMD ["npm", "start"] 