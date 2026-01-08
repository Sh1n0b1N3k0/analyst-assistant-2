import React, { useState } from 'react';
import './App.css';
import ImportForm from './components/ImportForm';
import ExportForm from './components/ExportForm';

function App() {
  const [activeTab, setActiveTab] = useState<'import' | 'export'>('import');

  return (
    <div className="App">
      <header className="App-header">
        <h1>Analyst Assistant</h1>
        <p>Система управления требованиями SRS</p>
      </header>
      
      <nav className="App-nav">
        <button
          className={activeTab === 'import' ? 'active' : ''}
          onClick={() => setActiveTab('import')}
        >
          Импорт требований
        </button>
        <button
          className={activeTab === 'export' ? 'active' : ''}
          onClick={() => setActiveTab('export')}
        >
          Экспорт требований
        </button>
      </nav>

      <main className="App-main">
        {activeTab === 'import' && <ImportForm />}
        {activeTab === 'export' && <ExportForm />}
      </main>
    </div>
  );
}

export default App;
