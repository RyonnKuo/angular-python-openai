import { TestBed } from '@angular/core/testing';

import { PythonCollectionService } from './python-collection.service';

describe('PythonCollectionService', () => {
  let service: PythonCollectionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PythonCollectionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
