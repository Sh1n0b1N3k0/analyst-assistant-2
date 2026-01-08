import React, { useState } from 'react';
import axios from 'axios';
import './ImportForm.css';

interface ImportFormProps {}

const ImportForm: React.FC<ImportFormProps> = () => {
  const [file, setFile] = useState<File | null>(null);
  const [fileType, setFileType] = useState<'json' | 'csv'>('json');
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);
  const [manualMode, setManualMode] = useState(false);
  const [manualData, setManualData] = useState({
    requirement_id: '',
    title: '',
    description: '',
    priority: '',
    status: 'Draft',
    category: '',
    source: '',
    stakeholder: ''
  });

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      const fileName = e.target.files[0].name.toLowerCase();
      if (fileName.endsWith('.json')) {
        setFileType('json');
      } else if (fileName.endsWith('.csv')) {
        setFileType('csv');
      }
    }
  };

  const handleFileImport = async () => {
    if (!file) {
      setMessage({ type: 'error', text: 'Пожалуйста, выберите файл' });
      return;
    }

    setLoading(true);
    setMessage(null);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const endpoint = fileType === 'json' 
        ? 'http://localhost:8000/api/import/json'
        : 'http://localhost:8000/api/import/csv';

      const response = await axios.post(endpoint, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setMessage({
        type: 'success',
        text: `Успешно импортировано требований: ${response.data.length}`
      });
      setFile(null);
    } catch (error: any) {
      setMessage({
        type: 'error',
        text: error.response?.data?.detail || 'Ошибка при импорте файла'
      });
    } finally {
      setLoading(false);
    }
  };

  const handleManualImport = async () => {
    if (!manualData.requirement_id || !manualData.title || !manualData.description) {
      setMessage({ type: 'error', text: 'Заполните обязательные поля' });
      return;
    }

    setLoading(true);
    setMessage(null);

    try {
      await axios.post('http://localhost:8000/api/import/manual', manualData);
      setMessage({ type: 'success', text: 'Требование успешно импортировано' });
      setManualData({
        requirement_id: '',
        title: '',
        description: '',
        priority: '',
        status: 'Draft',
        category: '',
        source: '',
        stakeholder: ''
      });
    } catch (error: any) {
      setMessage({
        type: 'error',
        text: error.response?.data?.detail || 'Ошибка при импорте требования'
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ImportForm">
      <div className="form-container">
        <div className="form-header">
          <h2>Импорт требований</h2>
          <button
            className="toggle-mode"
            onClick={() => setManualMode(!manualMode)}
          >
            {manualMode ? 'Импорт из файла' : 'Ручной ввод'}
          </button>
        </div>

        {message && (
          <div className={`message ${message.type}`}>
            {message.text}
          </div>
        )}

        {!manualMode ? (
          <div className="file-import">
            <div className="form-group">
              <label htmlFor="file">Выберите файл (JSON или CSV)</label>
              <input
                type="file"
                id="file"
                accept=".json,.csv"
                onChange={handleFileChange}
                disabled={loading}
              />
              {file && (
                <div className="file-info">
                  Выбран файл: {file.name}
                </div>
              )}
            </div>

            <button
              className="submit-button"
              onClick={handleFileImport}
              disabled={loading || !file}
            >
              {loading ? 'Импорт...' : 'Импортировать'}
            </button>
          </div>
        ) : (
          <div className="manual-import">
            <div className="form-group">
              <label htmlFor="requirement_id">ID требования *</label>
              <input
                type="text"
                id="requirement_id"
                value={manualData.requirement_id}
                onChange={(e) => setManualData({ ...manualData, requirement_id: e.target.value })}
                disabled={loading}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="title">Название *</label>
              <input
                type="text"
                id="title"
                value={manualData.title}
                onChange={(e) => setManualData({ ...manualData, title: e.target.value })}
                disabled={loading}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="description">Описание *</label>
              <textarea
                id="description"
                value={manualData.description}
                onChange={(e) => setManualData({ ...manualData, description: e.target.value })}
                disabled={loading}
                rows={5}
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="priority">Приоритет</label>
                <select
                  id="priority"
                  value={manualData.priority}
                  onChange={(e) => setManualData({ ...manualData, priority: e.target.value })}
                  disabled={loading}
                >
                  <option value="">Не указан</option>
                  <option value="High">High</option>
                  <option value="Medium">Medium</option>
                  <option value="Low">Low</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="status">Статус</label>
                <select
                  id="status"
                  value={manualData.status}
                  onChange={(e) => setManualData({ ...manualData, status: e.target.value })}
                  disabled={loading}
                >
                  <option value="Draft">Draft</option>
                  <option value="Approved">Approved</option>
                  <option value="Rejected">Rejected</option>
                  <option value="In Review">In Review</option>
                </select>
              </div>
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="category">Категория</label>
                <input
                  type="text"
                  id="category"
                  value={manualData.category}
                  onChange={(e) => setManualData({ ...manualData, category: e.target.value })}
                  disabled={loading}
                />
              </div>

              <div className="form-group">
                <label htmlFor="source">Источник</label>
                <input
                  type="text"
                  id="source"
                  value={manualData.source}
                  onChange={(e) => setManualData({ ...manualData, source: e.target.value })}
                  disabled={loading}
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="stakeholder">Заинтересованное лицо</label>
              <input
                type="text"
                id="stakeholder"
                value={manualData.stakeholder}
                onChange={(e) => setManualData({ ...manualData, stakeholder: e.target.value })}
                disabled={loading}
              />
            </div>

            <button
              className="submit-button"
              onClick={handleManualImport}
              disabled={loading}
            >
              {loading ? 'Импорт...' : 'Импортировать'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ImportForm;
