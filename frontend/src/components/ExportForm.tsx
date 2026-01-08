import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ExportForm.css';

interface ExportFormProps {}

interface ExportFilters {
  category: string;
  status: string;
  priority: string;
}

interface FilterOptions {
  categories: string[];
  statuses: string[];
  priorities: string[];
}

const ExportForm: React.FC<ExportFormProps> = () => {
  const [filters, setFilters] = useState<ExportFilters>({
    category: '',
    status: '',
    priority: ''
  });
  const [filterOptions, setFilterOptions] = useState<FilterOptions>({
    categories: [],
    statuses: [],
    priorities: []
  });
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  useEffect(() => {
    // Загружаем доступные значения для фильтров
    axios.get('http://localhost:8000/api/export/filters')
      .then(response => {
        setFilterOptions(response.data);
      })
      .catch(error => {
        console.error('Ошибка загрузки фильтров:', error);
      });
  }, []);

  const handleFilterChange = (field: keyof ExportFilters, value: string) => {
    setFilters(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const handleExport = async (format: 'json' | 'csv') => {
    setLoading(true);
    setMessage(null);

    try {
      const params = new URLSearchParams();
      if (filters.category) params.append('category', filters.category);
      if (filters.status) params.append('status', filters.status);
      if (filters.priority) params.append('priority', filters.priority);

      const endpoint = format === 'json'
        ? `http://localhost:8000/api/export/json/file?${params.toString()}`
        : `http://localhost:8000/api/export/csv/file?${params.toString()}`;

      const response = await axios.get(endpoint, {
        responseType: 'blob'
      });

      // Создаем ссылку для скачивания
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `requirements.${format}`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);

      setMessage({
        type: 'success',
        text: `Файл успешно экспортирован в формате ${format.toUpperCase()}`
      });
    } catch (error: any) {
      setMessage({
        type: 'error',
        text: error.response?.data?.detail || 'Ошибка при экспорте'
      });
    } finally {
      setLoading(false);
    }
  };

  const handlePreview = async () => {
    setLoading(true);
    setMessage(null);

    try {
      const params = new URLSearchParams();
      if (filters.category) params.append('category', filters.category);
      if (filters.status) params.append('status', filters.status);
      if (filters.priority) params.append('priority', filters.priority);

      const response = await axios.get(`http://localhost:8000/api/export/json?${params.toString()}`);
      
      setMessage({
        type: 'success',
        text: `Найдено требований: ${response.data.length}`
      });
    } catch (error: any) {
      setMessage({
        type: 'error',
        text: error.response?.data?.detail || 'Ошибка при получении данных'
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ExportForm">
      <div className="form-container">
        <div className="form-header">
          <h2>Экспорт требований</h2>
        </div>

        {message && (
          <div className={`message ${message.type}`}>
            {message.text}
          </div>
        )}

        <div className="filters-section">
          <h3>Фильтры экспорта</h3>
          <p className="filters-description">
            Выберите критерии для фильтрации требований при экспорте. 
            Оставьте поля пустыми для экспорта всех требований.
          </p>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="category">Категория</label>
              <select
                id="category"
                value={filters.category}
                onChange={(e) => handleFilterChange('category', e.target.value)}
                disabled={loading}
              >
                <option value="">Все категории</option>
                {filterOptions.categories.map(cat => (
                  <option key={cat} value={cat}>{cat}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="status">Статус</label>
              <select
                id="status"
                value={filters.status}
                onChange={(e) => handleFilterChange('status', e.target.value)}
                disabled={loading}
              >
                <option value="">Все статусы</option>
                {filterOptions.statuses.map(status => (
                  <option key={status} value={status}>{status}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="priority">Приоритет</label>
              <select
                id="priority"
                value={filters.priority}
                onChange={(e) => handleFilterChange('priority', e.target.value)}
                disabled={loading}
              >
                <option value="">Все приоритеты</option>
                {filterOptions.priorities.map(priority => (
                  <option key={priority} value={priority}>{priority}</option>
                ))}
              </select>
            </div>
          </div>

          <button
            className="preview-button"
            onClick={handlePreview}
            disabled={loading}
          >
            {loading ? 'Загрузка...' : 'Предпросмотр (количество)'}
          </button>
        </div>

        <div className="export-section">
          <h3>Формат экспорта</h3>
          <div className="export-buttons">
            <button
              className="export-button json"
              onClick={() => handleExport('json')}
              disabled={loading}
            >
              <span className="button-icon">📄</span>
              Экспорт в JSON
            </button>
            <button
              className="export-button csv"
              onClick={() => handleExport('csv')}
              disabled={loading}
            >
              <span className="button-icon">📊</span>
              Экспорт в CSV
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExportForm;
