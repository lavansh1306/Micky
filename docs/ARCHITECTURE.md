# Micky - Architecture Documentation

## System Architecture Overview

Micky follows a modern three-tier architecture with AI integration:

```
┌─────────────────────────────────────────────────────────────────┐
│                          USER LAYER                              │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  👤 User Interface                                    │       │
│  │  • Voice Input (Microphone)                          │       │
│  │  • Visual Feedback (Animated Circle)                 │       │
│  │  • Text Display (Response Text)                      │       │
│  │  • Speech Output (Audio)                             │       │
│  └──────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
                            ↕️
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND LAYER                            │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  🎨 HTML/CSS (UI Components)                         │       │
│  │  ├─ Animated Circle UI                               │       │
│  │  ├─ Visual Feedback Effects                          │       │
│  │  └─ Responsive Design                                │       │
│  └──────────────────────────────────────────────────────┘       │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  📱 JavaScript (Client Logic)                        │       │
│  │  ├─ Event Handlers                                   │       │
│  │  ├─ Speech Recognition                               │       │
│  │  ├─ Fetch API (HTTP Requests)                        │       │
│  │  ├─ Speech Synthesis                                 │       │
│  │  └─ Text Animation                                   │       │
│  └──────────────────────────────────────────────────────┘       │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  🌐 Browser APIs                                     │       │
│  │  ├─ Web Speech API (Recognition & Synthesis)         │       │
│  │  ├─ DOM Manipulation                                 │       │
│  │  └─ Fetch API                                        │       │
│  └──────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
                            ↕️ HTTP/JSON
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND LAYER                            │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  🐍 Flask Application (Python)                       │       │
│  │  ├─ app.py (Main Application)                        │       │
│  │  ├─ Route Handling                                   │       │
│  │  ├─ Request Processing                               │       │
│  │  └─ Response Formatting                              │       │
│  └──────────────────────────────────────────────────────┘       │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  🛣️  API Routes                                       │       │
│  │  ├─ GET  /         → Serve HTML                      │       │
│  │  └─ POST /micky    → Process Query & Return Response │       │
│  └──────────────────────────────────────────────────────┘       │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  🦄 Gunicorn (WSGI Server)                           │       │
│  │  ├─ Production HTTP Server                           │       │
│  │  ├─ Worker Processes                                 │       │
│  │  └─ Port Management                                  │       │
│  └──────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
                            ↕️ API Calls
┌─────────────────────────────────────────────────────────────────┐
│                          AI LAYER                                │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  🤖 Google Gemini AI (gemini-2.0-flash)             │       │
│  │  ├─ Natural Language Understanding                   │       │
│  │  ├─ Medical Knowledge Base                           │       │
│  │  ├─ Context Processing                               │       │
│  │  └─ Response Generation                              │       │
│  └──────────────────────────────────────────────────────┘       │
│  ┌──────────────────────────────────────────────────────┐       │
│  │  💬 Prompt Engineering                               │       │
│  │  ├─ Healthcare Context                               │       │
│  │  ├─ Safety Guidelines                                │       │
│  │  ├─ Response Format Rules                            │       │
│  │  └─ Ethical Constraints                              │       │
│  └──────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Sequence

### 1. User Voice Input → Frontend
```
User speaks → Microphone → Web Speech API → JavaScript
```

### 2. Frontend → Backend
```
JavaScript → Fetch API → POST /micky → Flask Server
```
**Request Format:**
```json
{
  "query": "I have a headache"
}
```

### 3. Backend → AI Processing
```
Flask → Prompt Construction → Google Gemini API → AI Processing
```

### 4. AI → Backend Response
```
Gemini AI → Generated Response → Flask Processing → JSON Response
```
**Response Format:**
```json
{
  "response": "Take paracetamol 500mg, stay hydrated, and rest in a dark room."
}
```

### 5. Backend → Frontend
```
Flask Response → JavaScript → Text Display + Speech Synthesis
```

### 6. Frontend → User Output
```
JavaScript → Web Speech API → Speaker → User hears response
JavaScript → DOM Update → Screen → User sees response
```

## Component Details

### Frontend Components

#### HTML/CSS (`templates/index.html`, `static/css/styles.css`)
- **Circle UI**: Animated center circle representing Micky
- **Ears**: Left and right decorative elements
- **Button**: "Talk to Micky" / "Stop Micky" toggle
- **Response Display**: Text area for AI responses
- **Styling**: Cyan/blue gradient theme with glow effects

#### JavaScript (`static/js/script.js`)
- **Speech Recognition**: Converts voice to text
- **API Communication**: Sends queries to backend
- **Speech Synthesis**: Converts text responses to speech
- **UI Animation**: Manages visual feedback during interaction
- **Text Effects**: Types out responses character by character

### Backend Components

#### Flask Application (`app.py`)
- **Web Framework**: Flask 2.2.5
- **Template Rendering**: Serves HTML interface
- **API Endpoint**: Processes POST requests to `/micky`
- **Environment Config**: Loads API keys and settings
- **Error Handling**: Manages API failures gracefully

#### Gunicorn Server
- **Production Server**: WSGI-compliant HTTP server
- **Process Management**: Handles multiple workers
- **Port Binding**: Configurable port (default 8080)
- **Auto-reload**: Development mode support

### AI Components

#### Google Gemini AI
- **Model**: gemini-2.0-flash
- **Capabilities**: 
  - Natural language understanding
  - Medical knowledge processing
  - Context-aware responses
  - Safety-filtered outputs

#### Prompt Engineering
- **System Prompt**: Defines Micky's personality and constraints
- **Healthcare Context**: Medical assistance specialization
- **Safety Rules**: Prevents harmful advice
- **Response Format**: Short, actionable answers (1-2 sentences)
- **Examples**: Includes few-shot learning examples

## Technology Stack

### Core Technologies

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Backend** | Python | 3.10 | Core programming language |
| **Web Framework** | Flask | 2.2.5 | RESTful API server |
| **WSGI Server** | Gunicorn | 21.2.0 | Production HTTP server |
| **AI Platform** | Google Gemini | 2.0-flash | AI response generation |
| **Frontend** | HTML5/CSS3/JS | ES6+ | User interface |

### AI/ML Libraries

| Library | Purpose |
|---------|---------|
| google-generativeai | Gemini API SDK |
| TensorFlow | Deep learning framework |
| PyTorch | Neural network library |
| Transformers | NLP models |
| scikit-learn | ML utilities |

### Data Processing

| Library | Purpose |
|---------|---------|
| NumPy | Numerical computing |
| Pandas | Data manipulation |
| SciPy | Scientific computing |
| Matplotlib | Visualization |

### Additional Tools

| Tool | Purpose |
|------|---------|
| Flask-CORS | Cross-origin requests |
| Flask-SocketIO | WebSocket support |
| Requests | HTTP client library |
| Protobuf | Data serialization |

## Security Considerations

### API Key Management
- Environment variables for sensitive data
- No hardcoded credentials
- Heroku config vars for deployment

### User Privacy
- No data logging or storage
- No user tracking
- Session-less architecture
- Client-side voice processing

### AI Safety
- Ethical prompt guidelines
- Controlled substance restrictions
- Disclaimer requirements
- Safe medical advice only

## Performance Characteristics

### Response Times
- Voice Recognition: Real-time (browser-native)
- API Processing: 1-3 seconds (network + AI)
- Speech Synthesis: Real-time (browser-native)
- Total Interaction: 3-5 seconds typical

### Scalability
- **Stateless Design**: Easy horizontal scaling
- **Gunicorn Workers**: Multi-process support
- **AI API**: Google's infrastructure handles load
- **Static Assets**: CDN-ready architecture

### Browser Compatibility
- Chrome/Edge: Full support (Web Speech API)
- Firefox: Full support with flag
- Safari: Partial support (iOS limitations)
- Mobile: Works on modern browsers

## Deployment Architecture

### Heroku Deployment
```
GitHub → Heroku Git → Build → Deploy → Run
                                   ↓
                            Dynos (Workers)
                                   ↓
                            Environment Vars
                                   ↓
                            Public URL
```

### Environment Variables
- `GEMINI_API_KEY`: Required for AI functionality
- `PORT`: Auto-assigned by Heroku or custom

### Scaling Options
- **Vertical**: Increase dyno size (RAM/CPU)
- **Horizontal**: Add more dynos (workers)
- **Auto-scaling**: Based on load metrics

## Future Enhancements

### Potential Improvements
1. **Multi-language Support**: Internationalization
2. **Chat History**: Session management
3. **User Accounts**: Personalized tracking
4. **Advanced UI**: More interactive visualizations
5. **Offline Mode**: Progressive Web App
6. **Mobile App**: Native iOS/Android versions
7. **Medical Database**: Integration with drug databases
8. **Emergency Routing**: Connect to local services

### Architecture Evolution
- Microservices separation
- Database integration
- Caching layer (Redis)
- Load balancing
- API rate limiting
- Analytics and monitoring

## Monitoring & Maintenance

### Logging
- Application logs via Gunicorn
- Error tracking
- API usage metrics
- Response time monitoring

### Health Checks
- Endpoint availability
- AI API connectivity
- Response validation
- Performance benchmarks

---

For the visual architecture diagram, see [architecture.svg](architecture.svg)
